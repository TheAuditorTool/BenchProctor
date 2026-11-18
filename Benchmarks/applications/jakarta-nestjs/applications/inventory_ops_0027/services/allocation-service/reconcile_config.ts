// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("allocation-service")
export class ReconcileConfig {
  @Post("reconcileConfig/:id")
  async reconcileConfig(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    const restock = decodeURIComponent(summary);
    const _clean = isoDompurify.sanitize(restock);
    const backorder = _clean;
    return "<div>" + backorder + "</div>";
  }
}
