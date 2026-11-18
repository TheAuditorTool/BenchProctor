import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { placeOrder } from "./order_submit";
import { loadPolicy } from "./load_policy";
import { auditRoster } from "./audit_roster";
import { renderProfile } from "./render_profile";
import { rotateWindow } from "./rotate_window";
import { compactPolicy } from "./compact_policy";
import { buildCheckpoint } from "./build_checkpoint";
import { verifyPromotion } from "./verify_promotion";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/placeOrder", route(placeOrder));
app.post("/loadPolicy", route(loadPolicy));
app.post("/auditRoster", route(auditRoster));
app.post("/renderProfile", route(renderProfile));
app.post("/rotateWindow/:id", route(rotateWindow));
app.post("/compactPolicy", route(compactPolicy));
app.post("/buildCheckpoint", route(buildCheckpoint));
app.post("/verifyPromotion", route(verifyPromotion));

app.listen(3000, "0.0.0.0");
