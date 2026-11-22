const express = require("express");
const session = require("express-session");

const declareCustoms = require("./customs_declare").declareCustoms;
const renderSummary = require("./render_summary").renderSummary;
const pruneSchedule = require("./prune_schedule").pruneSchedule;
const auditConfig = require("./audit_config").auditConfig;
const annotateHeader = require("./annotate_header").annotateHeader;
const exportCheckpoint = require("./export_checkpoint").exportCheckpoint;
const mergeCheckpoint = require("./merge_checkpoint").mergeCheckpoint;
const buildWaybill = require("./build_waybill").buildWaybill;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/declareCustoms/:id", route(declareCustoms));
app.post("/renderSummary", route(renderSummary));
app.post("/pruneSchedule", route(pruneSchedule));
app.post("/auditConfig", route(auditConfig));
app.post("/annotateHeader", route(annotateHeader));
app.post("/exportCheckpoint", route(exportCheckpoint));
app.post("/mergeCheckpoint", route(mergeCheckpoint));
app.post("/buildWaybill", route(buildWaybill));

app.listen(3000, "0.0.0.0");
