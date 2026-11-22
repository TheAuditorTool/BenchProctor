const express = require("express");
const session = require("express-session");

const buildStatement = require("./statement_build").buildStatement;
const reconcileWindow = require("./reconcile_window").reconcileWindow;
const summarizeSummary = require("./summarize_summary").summarizeSummary;
const validateCheckpoint = require("./validate_checkpoint").validateCheckpoint;
const resolveHeader = require("./resolve_header").resolveHeader;
const validateSchedule = require("./validate_schedule").validateSchedule;
const validateWindow = require("./validate_window").validateWindow;
const mergeSummary = require("./merge_summary").mergeSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/buildStatement", route(buildStatement));
app.post("/reconcileWindow", route(reconcileWindow));
app.post("/summarizeSummary", route(summarizeSummary));
app.post("/validateCheckpoint", route(validateCheckpoint));
app.post("/resolveHeader", route(resolveHeader));
app.post("/validateSchedule", route(validateSchedule));
app.post("/validateWindow", route(validateWindow));
app.post("/mergeSummary", route(mergeSummary));

app.listen(3000, "0.0.0.0");
