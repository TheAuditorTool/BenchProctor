// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("tracking-service")
export class PruneSummary {
  @Post("pruneSummary")
  async pruneSummary(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(caption);
    const consignment: string = readInput();
    return shared.escapeHtml(consignment);
  }
}
