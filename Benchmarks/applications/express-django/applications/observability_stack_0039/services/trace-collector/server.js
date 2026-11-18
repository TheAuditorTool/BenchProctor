const express = require("express");
const session = require("express-session");

const collectTrace = require("./trace_collect").collectTrace;
const reconcileSnapshot = require("./reconcile_snapshot").reconcileSnapshot;
const rotateBundle = require("./rotate_bundle").rotateBundle;
const renderReport = require("./render_report").renderReport;
const enrichTrace = require("./enrich_trace").enrichTrace;
const reconcileRoster = require("./reconcile_roster").reconcileRoster;
const exportWindow = require("./export_window").exportWindow;
const reconcileBatch = require("./reconcile_batch").reconcileBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/collectTrace", route(collectTrace));
app.post("/reconcileSnapshot", route(reconcileSnapshot));
app.post("/rotateBundle/:id", route(rotateBundle));
app.post("/renderReport", route(renderReport));
app.post("/enrichTrace", route(enrichTrace));
app.post("/reconcileRoster", route(reconcileRoster));
app.post("/exportWindow", route(exportWindow));
app.post("/reconcileBatch/:id", route(reconcileBatch));

app.listen(3000, "0.0.0.0");
