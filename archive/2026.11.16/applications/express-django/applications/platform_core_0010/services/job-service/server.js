const express = require("express");
const session = require("express-session");

const scheduleJob = require("./job_schedule").scheduleJob;
const auditCheckpoint = require("./audit_checkpoint").auditCheckpoint;
const compactProfile = require("./compact_profile").compactProfile;
const renderQuota = require("./render_quota").renderQuota;
const collectCheckpoint = require("./collect_checkpoint").collectCheckpoint;
const enrichRoster = require("./enrich_roster").enrichRoster;
const archiveReport = require("./archive_report").archiveReport;
const compactQuota = require("./compact_quota").compactQuota;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/scheduleJob", route(scheduleJob));
app.post("/auditCheckpoint", route(auditCheckpoint));
app.post("/compactProfile", route(compactProfile));
app.post("/renderQuota", route(renderQuota));
app.post("/collectCheckpoint", route(collectCheckpoint));
app.post("/enrichRoster", route(enrichRoster));
app.post("/archiveReport", route(archiveReport));
app.post("/compactQuota", route(compactQuota));

app.listen(3000, "0.0.0.0");
