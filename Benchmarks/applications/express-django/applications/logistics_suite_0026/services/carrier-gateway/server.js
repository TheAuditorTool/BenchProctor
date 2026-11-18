const express = require("express");
const session = require("express-session");

const dispatchCarrier = require("./carrier_dispatch").dispatchCarrier;
const summarizeSnapshot = require("./summarize_snapshot").summarizeSnapshot;
const reconcileManifest = require("./reconcile_manifest").reconcileManifest;
const resolveRecord = require("./resolve_record").resolveRecord;
const exportRecord = require("./export_record").exportRecord;
const archiveRoster = require("./archive_roster").archiveRoster;
const buildThreshold = require("./build_threshold").buildThreshold;
const auditReceipt = require("./audit_receipt").auditReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", route(dispatchCarrier));
app.post("/summarizeSnapshot", route(summarizeSnapshot));
app.post("/reconcileManifest", route(reconcileManifest));
app.post("/resolveRecord", route(resolveRecord));
app.post("/exportRecord", route(exportRecord));
app.post("/archiveRoster", route(archiveRoster));
app.post("/buildThreshold", route(buildThreshold));
app.post("/auditReceipt", route(auditReceipt));

app.listen(3000, "0.0.0.0");
