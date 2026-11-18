import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { shipLog } from "./log_ship";
import { loadSchedule } from "./load_schedule";
import { resolveWindow } from "./resolve_window";
import { verifyIndex } from "./verify_index";
import { normalizeAlert } from "./normalize_alert";
import { loadThreshold } from "./load_threshold";
import { rotatePolicy } from "./rotate_policy";
import { mergeSummary } from "./merge_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/shipLog", route(shipLog));
app.post("/loadSchedule", route(loadSchedule));
app.post("/resolveWindow", route(resolveWindow));
app.post("/verifyIndex", route(verifyIndex));
app.post("/normalizeAlert", route(normalizeAlert));
app.post("/loadThreshold", route(loadThreshold));
app.post("/rotatePolicy", route(rotatePolicy));
app.post("/mergeSummary", route(mergeSummary));

app.listen(3000, "0.0.0.0");
