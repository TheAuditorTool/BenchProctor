// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("retention-service")
export class ReconcileReport {
  @Post("reconcileReport/:id")
  async reconcileReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const cohort: string = readInput();
    return shared.escapeHtml(cohort);
  }
}
