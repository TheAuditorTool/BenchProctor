const express = require("express");
const session = require("express-session");

const reviewEditorial = require("./editorial_review").reviewEditorial;
const reconcileProfile = require("./reconcile_profile").reconcileProfile;
const auditLedger = require("./audit_ledger").auditLedger;
const buildSnapshot = require("./build_snapshot").buildSnapshot;
const exportRoster = require("./export_roster").exportRoster;
const enrichReport = require("./enrich_report").enrichReport;
const summarizeSummary = require("./summarize_summary").summarizeSummary;
const annotateThreshold = require("./annotate_threshold").annotateThreshold;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/reviewEditorial", route(reviewEditorial));
app.post("/reconcileProfile", route(reconcileProfile));
app.post("/auditLedger", route(auditLedger));
app.post("/buildSnapshot", route(buildSnapshot));
app.post("/exportRoster", route(exportRoster));
app.post("/enrichReport", route(enrichReport));
app.post("/summarizeSummary", route(summarizeSummary));
app.post("/annotateThreshold", route(annotateThreshold));

app.listen(3000, "0.0.0.0");
