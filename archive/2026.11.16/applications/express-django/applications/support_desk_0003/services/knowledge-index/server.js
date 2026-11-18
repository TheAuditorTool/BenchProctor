const express = require("express");
const session = require("express-session");

const searchKnowledge = require("./knowledge_search").searchKnowledge;
const archiveSurvey = require("./archive_survey").archiveSurvey;
const renderThreshold = require("./render_threshold").renderThreshold;
const annotateMacro = require("./annotate_macro").annotateMacro;
const archiveSnapshot = require("./archive_snapshot").archiveSnapshot;
const archiveTicket = require("./archive_ticket").archiveTicket;
const summarizeDigest = require("./summarize_digest").summarizeDigest;
const reconcileLedger = require("./reconcile_ledger").reconcileLedger;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/searchKnowledge", route(searchKnowledge));
app.post("/archiveSurvey", route(archiveSurvey));
app.post("/renderThreshold", route(renderThreshold));
app.post("/annotateMacro", route(annotateMacro));
app.post("/archiveSnapshot", route(archiveSnapshot));
app.post("/archiveTicket", route(archiveTicket));
app.post("/summarizeDigest", route(summarizeDigest));
app.post("/reconcileLedger", route(reconcileLedger));

app.listen(3000, "0.0.0.0");
