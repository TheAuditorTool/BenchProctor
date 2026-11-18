const express = require("express");
const session = require("express-session");

const buildManifest = require("./manifest_build").buildManifest;
const rotateWindow = require("./rotate_window").rotateWindow;
const validateSummary = require("./validate_summary").validateSummary;
const publishReceipt = require("./publish_receipt").publishReceipt;
const reconcileCheckpoint = require("./reconcile_checkpoint").reconcileCheckpoint;
const validateProfile = require("./validate_profile").validateProfile;
const buildHeader = require("./build_header").buildHeader;
const archiveThreshold = require("./archive_threshold").archiveThreshold;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/buildManifest", route(buildManifest));
app.post("/rotateWindow", route(rotateWindow));
app.post("/validateSummary", route(validateSummary));
app.post("/publishReceipt", route(publishReceipt));
app.post("/reconcileCheckpoint", route(reconcileCheckpoint));
app.post("/validateProfile", route(validateProfile));
app.post("/buildHeader", route(buildHeader));
app.post("/archiveThreshold", route(archiveThreshold));

app.listen(3000, "0.0.0.0");
