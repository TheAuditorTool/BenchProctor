const express = require("express");
const session = require("express-session");

const composeTemplate = require("./template_compose").composeTemplate;
const renderProfile = require("./render_profile").renderProfile;
const rotateDelivery = require("./rotate_delivery").rotateDelivery;
const validateSchedule = require("./validate_schedule").validateSchedule;
const validatePolicy = require("./validate_policy").validatePolicy;
const validateMessage = require("./validate_message").validateMessage;
const annotateSchedule = require("./annotate_schedule").annotateSchedule;
const loadRecord = require("./load_record").loadRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/composeTemplate", route(composeTemplate));
app.post("/renderProfile/:id", route(renderProfile));
app.post("/rotateDelivery", route(rotateDelivery));
app.post("/validateSchedule", route(validateSchedule));
app.post("/validatePolicy", route(validatePolicy));
app.post("/validateMessage", route(validateMessage));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/loadRecord", route(loadRecord));

app.listen(3000, "0.0.0.0");
