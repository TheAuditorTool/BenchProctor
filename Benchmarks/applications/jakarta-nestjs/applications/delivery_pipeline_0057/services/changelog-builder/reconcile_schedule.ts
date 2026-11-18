// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("changelog-builder")
export class ReconcileSchedule {
  @Post("reconcileSchedule")
  async reconcileSchedule(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.multipart_field as string) || "";
    const wording = footnote != null ? footnote : '';
    JSON.parse(wording);
    return { created: true };
  }
}
