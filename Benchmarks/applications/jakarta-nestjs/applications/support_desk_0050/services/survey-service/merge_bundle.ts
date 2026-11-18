// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("survey-service")
export class MergeBundle {
  @Post("mergeBundle/:id")
  async mergeBundle(@Req() req: Request): Promise<unknown> {
    const remark = (req.params.id as string) || "";
    const inquiry = decodeURIComponent(remark);
    const _clean = isoDompurify.sanitize(inquiry);
    const grievance = _clean;
    return "<div>" + grievance + "</div>";
  }
}
