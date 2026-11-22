const express = require("express");
const session = require("express-session");

const pollTracking = require("./tracking_poll").pollTracking;
const archiveReport = require("./archive_report").archiveReport;
const enrichWindow = require("./enrich_window").enrichWindow;
const loadSchedule = require("./load_schedule").loadSchedule;
const pruneSummary = require("./prune_summary").pruneSummary;
const fetchLedger = require("./fetch_ledger").fetchLedger;
const exportBundle = require("./export_bundle").exportBundle;
const loadDigest = require("./load_digest").loadDigest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/pollTracking", route(pollTracking));
app.post("/archiveReport", route(archiveReport));
app.post("/enrichWindow", route(enrichWindow));
app.post("/loadSchedule", route(loadSchedule));
app.post("/pruneSummary", route(pruneSummary));
app.post("/fetchLedger", route(fetchLedger));
app.post("/exportBundle", route(exportBundle));
app.post("/loadDigest", route(loadDigest));

app.listen(3000, "0.0.0.0");
