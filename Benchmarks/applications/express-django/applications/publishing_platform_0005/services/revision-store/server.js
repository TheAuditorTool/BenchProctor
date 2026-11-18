const express = require("express");
const session = require("express-session");

const saveRevision = require("./revision_save").saveRevision;
const rotateSnapshot = require("./rotate_snapshot").rotateSnapshot;
const publishManifest = require("./publish_manifest").publishManifest;
const pruneThreshold = require("./prune_threshold").pruneThreshold;
const formatRevision = require("./format_revision").formatRevision;
const auditManifest = require("./audit_manifest").auditManifest;
const pruneArticle = require("./prune_article").pruneArticle;
const publishWindow = require("./publish_window").publishWindow;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/saveRevision/:id", route(saveRevision));
app.post("/rotateSnapshot", route(rotateSnapshot));
app.post("/publishManifest", route(publishManifest));
app.post("/pruneThreshold", route(pruneThreshold));
app.post("/formatRevision", route(formatRevision));
app.post("/auditManifest", route(auditManifest));
app.post("/pruneArticle", route(pruneArticle));
app.post("/publishWindow", route(publishWindow));

app.listen(3000, "0.0.0.0");
