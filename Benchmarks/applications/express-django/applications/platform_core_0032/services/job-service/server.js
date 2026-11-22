const express = require("express");
const session = require("express-session");

const scheduleJob = require("./job_schedule").scheduleJob;
const buildHeader = require("./build_header").buildHeader;
const publishCheckpoint = require("./publish_checkpoint").publishCheckpoint;
const annotateSnapshot = require("./annotate_snapshot").annotateSnapshot;
const collectQuota = require("./collect_quota").collectQuota;
const mergeProfile = require("./merge_profile").mergeProfile;
const mergeReport = require("./merge_report").mergeReport;
const buildSummary = require("./build_summary").buildSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/scheduleJob", route(scheduleJob));
app.post("/buildHeader", route(buildHeader));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/annotateSnapshot", route(annotateSnapshot));
app.post("/collectQuota", route(collectQuota));
app.post("/mergeProfile", route(mergeProfile));
app.post("/mergeReport", route(mergeReport));
app.post("/buildSummary", route(buildSummary));

app.listen(3000, "0.0.0.0");
