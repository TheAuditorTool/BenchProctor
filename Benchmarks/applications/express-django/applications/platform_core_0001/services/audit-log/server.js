const express = require("express");
const session = require("express-session");

const appendAudit = require("./audit_append").appendAudit;
const exportRoster = require("./export_roster").exportRoster;
const compactHeader = require("./compact_header").compactHeader;
const annotateSchedule = require("./annotate_schedule").annotateSchedule;
const collectDigest = require("./collect_digest").collectDigest;
const buildConfig = require("./build_config").buildConfig;
const pruneRecord = require("./prune_record").pruneRecord;
const auditManifest = require("./audit_manifest").auditManifest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/appendAudit", route(appendAudit));
app.post("/exportRoster", route(exportRoster));
app.post("/compactHeader", route(compactHeader));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/collectDigest", route(collectDigest));
app.post("/buildConfig", route(buildConfig));
app.post("/pruneRecord", route(pruneRecord));
app.post("/auditManifest", route(auditManifest));

app.listen(3000, "0.0.0.0");
