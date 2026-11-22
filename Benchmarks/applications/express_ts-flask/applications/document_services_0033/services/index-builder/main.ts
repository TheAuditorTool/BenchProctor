import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { indexDocument } from "./search_index";
import { rotateConversion } from "./rotate_conversion";
import { rotateSchedule } from "./rotate_schedule";
import { archiveSignature } from "./archive_signature";
import { buildRoster } from "./build_roster";
import { reconcileWindow } from "./reconcile_window";
import { buildThreshold } from "./build_threshold";
import { renderConversion } from "./render_conversion";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/indexDocument", route(indexDocument));
app.post("/rotateConversion", route(rotateConversion));
app.post("/rotateSchedule", route(rotateSchedule));
app.post("/archiveSignature", route(archiveSignature));
app.post("/buildRoster", route(buildRoster));
app.post("/reconcileWindow", route(reconcileWindow));
app.post("/buildThreshold", route(buildThreshold));
app.post("/renderConversion/:id", route(renderConversion));

app.listen(3000, "0.0.0.0");
