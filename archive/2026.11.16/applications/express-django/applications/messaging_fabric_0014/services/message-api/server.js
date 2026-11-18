const express = require("express");
const session = require("express-session");

const publishMessage = require("./message_publish").publishMessage;
const annotateRoster = require("./annotate_roster").annotateRoster;
const summarizeBundle = require("./summarize_bundle").summarizeBundle;
const resolveBatch = require("./resolve_batch").resolveBatch;
const pruneReport = require("./prune_report").pruneReport;
const loadLedger = require("./load_ledger").loadLedger;
const summarizeManifest = require("./summarize_manifest").summarizeManifest;
const reconcileSchedule = require("./reconcile_schedule").reconcileSchedule;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/publishMessage", route(publishMessage));
app.post("/annotateRoster", route(annotateRoster));
app.post("/summarizeBundle", route(summarizeBundle));
app.post("/resolveBatch", route(resolveBatch));
app.post("/pruneReport", route(pruneReport));
app.post("/loadLedger", route(loadLedger));
app.post("/summarizeManifest", route(summarizeManifest));
app.post("/reconcileSchedule", route(reconcileSchedule));

app.listen(3000, "0.0.0.0");
