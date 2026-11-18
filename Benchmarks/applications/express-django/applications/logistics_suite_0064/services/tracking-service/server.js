const express = require("express");
const session = require("express-session");

const pollTracking = require("./tracking_poll").pollTracking;
const buildRecord = require("./build_record").buildRecord;
const rotateLabel = require("./rotate_label").rotateLabel;
const compactPolicy = require("./compact_policy").compactPolicy;
const auditBatch = require("./audit_batch").auditBatch;
const collectProfile = require("./collect_profile").collectProfile;
const compactThreshold = require("./compact_threshold").compactThreshold;
const archiveRecord = require("./archive_record").archiveRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/pollTracking", route(pollTracking));
app.post("/buildRecord", route(buildRecord));
app.post("/rotateLabel/:id", route(rotateLabel));
app.post("/compactPolicy", route(compactPolicy));
app.post("/auditBatch", route(auditBatch));
app.post("/collectProfile", route(collectProfile));
app.post("/compactThreshold", route(compactThreshold));
app.post("/archiveRecord", route(archiveRecord));

app.listen(3000, "0.0.0.0");
