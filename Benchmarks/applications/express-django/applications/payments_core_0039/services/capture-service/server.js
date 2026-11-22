const express = require("express");
const session = require("express-session");
const multer = require("multer");

const settleCapture = require("./capture_settle").settleCapture;
const compactHeader = require("./compact_header").compactHeader;
const rotateThreshold = require("./rotate_threshold").rotateThreshold;
const annotateCheckpoint = require("./annotate_checkpoint").annotateCheckpoint;
const buildConfig = require("./build_config").buildConfig;
const archiveSchedule = require("./archive_schedule").archiveSchedule;
const verifyDigest = require("./verify_digest").verifyDigest;
const collectIndex = require("./collect_index").collectIndex;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/settleCapture", route(settleCapture));
app.post("/compactHeader", route(compactHeader));
app.post("/rotateThreshold", route(rotateThreshold));
app.post("/annotateCheckpoint", route(annotateCheckpoint));
app.post("/buildConfig", route(buildConfig));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/verifyDigest", route(verifyDigest));
app.post("/collectIndex", route(collectIndex));

app.listen(3000, "0.0.0.0");
