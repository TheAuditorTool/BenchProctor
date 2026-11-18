// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("fx-service")
export class ReconcileConfig {
  @Post("reconcileConfig/:id")
  async reconcileConfig(@Req() req: Request): Promise<unknown> {
    const headline = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(headline);
    const disbursement: string = readInput();
    return shared.escapeHtml(disbursement);
  }
}
