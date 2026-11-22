const express = require("express");
const session = require("express-session");
const multer = require("multer");

const ingestMetric = require("./metric_ingest").ingestMetric;
const validateAlert = require("./validate_alert").validateAlert;
const enrichReport = require("./enrich_report").enrichReport;
const buildThreshold = require("./build_threshold").buildThreshold;
const archiveIndex = require("./archive_index").archiveIndex;
const resolveBundle = require("./resolve_bundle").resolveBundle;
const renderCheckpoint = require("./render_checkpoint").renderCheckpoint;
const rotateThreshold = require("./rotate_threshold").rotateThreshold;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/ingestMetric", route(ingestMetric));
app.post("/validateAlert", route(validateAlert));
app.post("/enrichReport", route(enrichReport));
app.post("/buildThreshold", route(buildThreshold));
app.post("/archiveIndex", route(archiveIndex));
app.post("/resolveBundle", route(resolveBundle));
app.post("/renderCheckpoint", route(renderCheckpoint));
app.post("/rotateThreshold", route(rotateThreshold));

app.listen(3000, "0.0.0.0");
