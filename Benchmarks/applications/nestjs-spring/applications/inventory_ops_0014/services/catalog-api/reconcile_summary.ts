// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("catalog-api")
export class ReconcileSummary {
  @Post("reconcileSummary")
  async reconcileSummary(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(excerpt);
    const restock: string = readInput();
    return shared.escapeHtml(restock);
  }
}
