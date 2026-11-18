const express = require("express");
const session = require("express-session");

const storeAttachment = require("./attachment_store").storeAttachment;
const enrichHeader = require("./enrich_header").enrichHeader;
const enrichCheckpoint = require("./enrich_checkpoint").enrichCheckpoint;
const publishSurvey = require("./publish_survey").publishSurvey;
const loadHeader = require("./load_header").loadHeader;
const auditSurvey = require("./audit_survey").auditSurvey;
const pruneRecord = require("./prune_record").pruneRecord;
const renderEscalation = require("./render_escalation").renderEscalation;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/storeAttachment", route(storeAttachment));
app.post("/enrichHeader", route(enrichHeader));
app.post("/enrichCheckpoint", route(enrichCheckpoint));
app.post("/publishSurvey/:id", route(publishSurvey));
app.post("/loadHeader", route(loadHeader));
app.post("/auditSurvey", route(auditSurvey));
app.post("/pruneRecord", route(pruneRecord));
app.post("/renderEscalation", route(renderEscalation));

app.listen(3000, "0.0.0.0");
