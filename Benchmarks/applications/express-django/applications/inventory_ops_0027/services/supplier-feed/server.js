const express = require("express");
const session = require("express-session");

const pullSupplierFeed = require("./supplier_feed").pullSupplierFeed;
const collectRecord = require("./collect_record").collectRecord;
const auditHeader = require("./audit_header").auditHeader;
const resolveRoster = require("./resolve_roster").resolveRoster;
const summarizeSchedule = require("./summarize_schedule").summarizeSchedule;
const buildReport = require("./build_report").buildReport;
const rotateSnapshot = require("./rotate_snapshot").rotateSnapshot;
const archivePolicy = require("./archive_policy").archivePolicy;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/pullSupplierFeed", route(pullSupplierFeed));
app.post("/collectRecord", route(collectRecord));
app.post("/auditHeader", route(auditHeader));
app.post("/resolveRoster", route(resolveRoster));
app.post("/summarizeSchedule", route(summarizeSchedule));
app.post("/buildReport", route(buildReport));
app.post("/rotateSnapshot", route(rotateSnapshot));
app.post("/archivePolicy", route(archivePolicy));

app.listen(3000, "0.0.0.0");
