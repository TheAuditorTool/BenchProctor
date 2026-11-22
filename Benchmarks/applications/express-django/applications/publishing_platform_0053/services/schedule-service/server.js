const express = require("express");
const session = require("express-session");

const schedulePublication = require("./publish_schedule").schedulePublication;
const resolveSchedule = require("./resolve_schedule").resolveSchedule;
const normalizeCheckpoint = require("./normalize_checkpoint").normalizeCheckpoint;
const publishReport = require("./publish_report").publishReport;
const normalizePolicy = require("./normalize_policy").normalizePolicy;
const publishSnapshot = require("./publish_snapshot").publishSnapshot;
const fetchReceipt = require("./fetch_receipt").fetchReceipt;
const reconcileArticle = require("./reconcile_article").reconcileArticle;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/schedulePublication", route(schedulePublication));
app.post("/resolveSchedule", route(resolveSchedule));
app.post("/normalizeCheckpoint", route(normalizeCheckpoint));
app.post("/publishReport", route(publishReport));
app.post("/normalizePolicy", route(normalizePolicy));
app.post("/publishSnapshot", route(publishSnapshot));
app.post("/fetchReceipt", route(fetchReceipt));
app.post("/reconcileArticle", route(reconcileArticle));

app.listen(3000, "0.0.0.0");
