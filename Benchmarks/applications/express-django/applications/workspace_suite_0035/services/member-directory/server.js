const express = require("express");
const session = require("express-session");
const multer = require("multer");

const inviteMember = require("./member_invite").inviteMember;
const annotateSummary = require("./annotate_summary").annotateSummary;
const normalizeRoster = require("./normalize_roster").normalizeRoster;
const renderDigest = require("./render_digest").renderDigest;
const enrichRoster = require("./enrich_roster").enrichRoster;
const verifyHeader = require("./verify_header").verifyHeader;
const renderThreshold = require("./render_threshold").renderThreshold;
const compactSchedule = require("./compact_schedule").compactSchedule;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/inviteMember", route(inviteMember));
app.post("/annotateSummary", route(annotateSummary));
app.post("/normalizeRoster", route(normalizeRoster));
app.post("/renderDigest", route(renderDigest));
app.post("/enrichRoster", route(enrichRoster));
app.post("/verifyHeader", route(verifyHeader));
app.post("/renderThreshold", route(renderThreshold));
app.post("/compactSchedule", route(compactSchedule));

app.listen(3000, "0.0.0.0");
