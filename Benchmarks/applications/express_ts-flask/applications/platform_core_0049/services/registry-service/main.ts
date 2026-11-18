import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { registerService } from "./service_register";
import { verifySchedule } from "./verify_schedule";
import { verifyReceipt } from "./verify_receipt";
import { validateHeader } from "./validate_header";
import { buildLedger } from "./build_ledger";
import { collectProfile } from "./collect_profile";
import { exportConfig } from "./export_config";
import { buildReport } from "./build_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerService", route(registerService));
app.post("/verifySchedule", route(verifySchedule));
app.post("/verifyReceipt/:id", route(verifyReceipt));
app.post("/validateHeader", route(validateHeader));
app.post("/buildLedger", route(buildLedger));
app.post("/collectProfile", route(collectProfile));
app.post("/exportConfig", route(exportConfig));
app.post("/buildReport", route(buildReport));

app.listen(3000, "0.0.0.0");
