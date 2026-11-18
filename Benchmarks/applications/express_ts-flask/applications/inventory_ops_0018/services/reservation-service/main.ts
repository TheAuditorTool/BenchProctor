import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { holdReservation } from "./reservation_hold";
import { formatHeader } from "./format_header";
import { annotateReport } from "./annotate_report";
import { verifyProfile } from "./verify_profile";
import { reconcileSchedule } from "./reconcile_schedule";
import { normalizeSchedule } from "./normalize_schedule";
import { buildSchedule } from "./build_schedule";
import { loadReservation } from "./load_reservation";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/holdReservation", route(holdReservation));
app.post("/formatHeader", route(formatHeader));
app.post("/annotateReport", route(annotateReport));
app.post("/verifyProfile", route(verifyProfile));
app.post("/reconcileSchedule", route(reconcileSchedule));
app.post("/normalizeSchedule", route(normalizeSchedule));
app.post("/buildSchedule", route(buildSchedule));
app.post("/loadReservation", route(loadReservation));

app.listen(3000, "0.0.0.0");
