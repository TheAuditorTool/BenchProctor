const express = require("express");
const session = require("express-session");

const collectTrace = require("./trace_collect").collectTrace;
const fetchReport = require("./fetch_report").fetchReport;
const pruneDigest = require("./prune_digest").pruneDigest;
const compactSchedule = require("./compact_schedule").compactSchedule;
const formatProfile = require("./format_profile").formatProfile;
const collectMetric = require("./collect_metric").collectMetric;
const pruneProfile = require("./prune_profile").pruneProfile;
const summarizeRoster = require("./summarize_roster").summarizeRoster;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/collectTrace", collectTrace);
app.post("/fetchReport", fetchReport);
app.post("/pruneDigest/:id", pruneDigest);
app.post("/compactSchedule", compactSchedule);
app.post("/formatProfile", formatProfile);
app.post("/collectMetric", collectMetric);
app.post("/pruneProfile", pruneProfile);
app.post("/summarizeRoster", summarizeRoster);

app.listen(3000, "0.0.0.0");
