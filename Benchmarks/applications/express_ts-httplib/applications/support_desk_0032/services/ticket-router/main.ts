import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { routeTicket } from "./ticket_route";
import { reconcileCheckpoint } from "./reconcile_checkpoint";
import { pruneHeader } from "./prune_header";
import { enrichBundle } from "./enrich_bundle";
import { resolveSurvey } from "./resolve_survey";
import { pruneSnapshot } from "./prune_snapshot";
import { validateBundle } from "./validate_bundle";
import { pruneReceipt } from "./prune_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/routeTicket", route(routeTicket));
app.post("/reconcileCheckpoint", route(reconcileCheckpoint));
app.post("/pruneHeader", route(pruneHeader));
app.post("/enrichBundle", route(enrichBundle));
app.post("/resolveSurvey", route(resolveSurvey));
app.post("/pruneSnapshot", route(pruneSnapshot));
app.post("/validateBundle", route(validateBundle));
app.post("/pruneReceipt", route(pruneReceipt));

app.listen(3000, "0.0.0.0");
