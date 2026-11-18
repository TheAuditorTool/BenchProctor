const express = require("express");
const session = require("express-session");

const publishArtifact = require("./artifact_publish").publishArtifact;
const formatApproval = require("./format_approval").formatApproval;
const archiveBatch = require("./archive_batch").archiveBatch;
const publishHeader = require("./publish_header").publishHeader;
const exportReport = require("./export_report").exportReport;
const rotateManifest = require("./rotate_manifest").rotateManifest;
const formatWindow = require("./format_window").formatWindow;
const pruneHeader = require("./prune_header").pruneHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/publishArtifact", route(publishArtifact));
app.post("/formatApproval", route(formatApproval));
app.post("/archiveBatch", route(archiveBatch));
app.post("/publishHeader", route(publishHeader));
app.post("/exportReport", route(exportReport));
app.post("/rotateManifest", route(rotateManifest));
app.post("/formatWindow", route(formatWindow));
app.post("/pruneHeader", route(pruneHeader));

app.listen(3000, "0.0.0.0");
