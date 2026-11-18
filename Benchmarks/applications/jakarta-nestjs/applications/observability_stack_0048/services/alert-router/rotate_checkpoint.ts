// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("alert-router")
export class RotateCheckpoint {
  @Post("rotateCheckpoint/:id")
  async rotateCheckpoint(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.params.id as string) || "";
    const gauge = decodeURIComponent(excerpt);
    const _clean = isoDompurify.sanitize(gauge);
    const cohort = _clean;
    return "<div>" + cohort + "</div>";
  }
}
