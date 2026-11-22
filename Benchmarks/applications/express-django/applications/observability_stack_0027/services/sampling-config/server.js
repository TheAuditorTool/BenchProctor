const express = require("express");
const session = require("express-session");

const configureSample = require("./sample_config").configureSample;
const fetchConfig = require("./fetch_config").fetchConfig;
const annotateReport = require("./annotate_report").annotateReport;
const compactIndex = require("./compact_index").compactIndex;
const reconcileThreshold = require("./reconcile_threshold").reconcileThreshold;
const enrichSchedule = require("./enrich_schedule").enrichSchedule;
const renderBundle = require("./render_bundle").renderBundle;
const collectSample = require("./collect_sample").collectSample;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/configureSample", route(configureSample));
app.post("/fetchConfig", route(fetchConfig));
app.post("/annotateReport", route(annotateReport));
app.post("/compactIndex", route(compactIndex));
app.post("/reconcileThreshold", route(reconcileThreshold));
app.post("/enrichSchedule", route(enrichSchedule));
app.post("/renderBundle", route(renderBundle));
app.post("/collectSample", route(collectSample));

app.listen(3000, "0.0.0.0");
