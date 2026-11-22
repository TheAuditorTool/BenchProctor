import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { attachAsset } from "./asset_attach";
import { mergeConfig } from "./merge_config";
import { validateWindow } from "./validate_window";
import { summarizeConfig } from "./summarize_config";
import { fetchThreshold } from "./fetch_threshold";
import { renderReport } from "./render_report";
import { verifySnapshot } from "./verify_snapshot";
import { collectWindow } from "./collect_window";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/attachAsset", route(attachAsset));
app.post("/mergeConfig", route(mergeConfig));
app.post("/validateWindow", route(validateWindow));
app.post("/summarizeConfig", route(summarizeConfig));
app.post("/fetchThreshold", route(fetchThreshold));
app.post("/renderReport", route(renderReport));
app.post("/verifySnapshot", route(verifySnapshot));
app.post("/collectWindow", route(collectWindow));

app.listen(3000, "0.0.0.0");
