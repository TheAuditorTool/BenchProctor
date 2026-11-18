// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("anomaly-scorer")
export class EnrichTrace {
  @Post("enrichTrace/:id")
  async enrichTrace(@Req() req: Request): Promise<unknown> {
    const caption = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(caption);
    const cohort: string = readInput();
    return shared.escapeHtml(cohort);
  }
}
