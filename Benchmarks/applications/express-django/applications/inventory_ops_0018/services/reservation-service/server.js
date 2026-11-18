const express = require("express");
const session = require("express-session");

const holdReservation = require("./reservation_hold").holdReservation;
const formatHeader = require("./format_header").formatHeader;
const annotateReport = require("./annotate_report").annotateReport;
const verifyProfile = require("./verify_profile").verifyProfile;
const reconcileSchedule = require("./reconcile_schedule").reconcileSchedule;
const normalizeSchedule = require("./normalize_schedule").normalizeSchedule;
const buildSchedule = require("./build_schedule").buildSchedule;
const loadReservation = require("./load_reservation").loadReservation;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/holdReservation", route(holdReservation));
app.post("/formatHeader", route(formatHeader));
app.post("/annotateReport", route(annotateReport));
app.post("/verifyProfile", route(verifyProfile));
app.post("/reconcileSchedule", route(reconcileSchedule));
app.post("/normalizeSchedule", route(normalizeSchedule));
app.post("/buildSchedule", route(buildSchedule));
app.post("/loadReservation/:id", route(loadReservation));

app.listen(3000, "0.0.0.0");
