// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("allocation-service")
export class ReconcileDigest {
  @Post("reconcileDigest/:id")
  async reconcileDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const restock: string = readInput();
    return shared.escapeHtml(restock);
  }
}
