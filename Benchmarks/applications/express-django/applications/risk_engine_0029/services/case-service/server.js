const express = require("express");
const session = require("express-session");

const openCase = require("./case_open").openCase;
const summarizeConfig = require("./summarize_config").summarizeConfig;
const rotateProfile = require("./rotate_profile").rotateProfile;
const auditWindow = require("./audit_window").auditWindow;
const reconcileRecord = require("./reconcile_record").reconcileRecord;
const enrichSchedule = require("./enrich_schedule").enrichSchedule;
const validateManifest = require("./validate_manifest").validateManifest;
const verifyIndex = require("./verify_index").verifyIndex;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/openCase", route(openCase));
app.post("/summarizeConfig/:id", route(summarizeConfig));
app.post("/rotateProfile", route(rotateProfile));
app.post("/auditWindow", route(auditWindow));
app.post("/reconcileRecord", route(reconcileRecord));
app.post("/enrichSchedule", route(enrichSchedule));
app.post("/validateManifest", route(validateManifest));
app.post("/verifyIndex", route(verifyIndex));

app.listen(3000, "0.0.0.0");
