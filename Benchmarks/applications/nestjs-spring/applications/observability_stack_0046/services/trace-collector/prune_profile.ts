// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("trace-collector")
export class PruneProfile {
  @Post("pruneProfile")
  async pruneProfile(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(paragraph);
    const gauge: string = readInput();
    return shared.escapeHtml(gauge);
  }
}
