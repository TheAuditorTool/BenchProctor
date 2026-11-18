const express = require("express");
const session = require("express-session");

const sweepRetention = require("./retention_sweep").sweepRetention;
const rotateCheckpoint = require("./rotate_checkpoint").rotateCheckpoint;
const validateCheckpoint = require("./validate_checkpoint").validateCheckpoint;
const compactBatch = require("./compact_batch").compactBatch;
const archiveSchedule = require("./archive_schedule").archiveSchedule;
const annotateHeader = require("./annotate_header").annotateHeader;
const collectReport = require("./collect_report").collectReport;
const fetchThreshold = require("./fetch_threshold").fetchThreshold;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/sweepRetention", route(sweepRetention));
app.post("/rotateCheckpoint", route(rotateCheckpoint));
app.post("/validateCheckpoint", route(validateCheckpoint));
app.post("/compactBatch", route(compactBatch));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/annotateHeader", route(annotateHeader));
app.post("/collectReport", route(collectReport));
app.post("/fetchThreshold", route(fetchThreshold));

app.listen(3000, "0.0.0.0");
