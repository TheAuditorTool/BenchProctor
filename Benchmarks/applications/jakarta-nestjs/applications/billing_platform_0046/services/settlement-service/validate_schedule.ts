// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("settlement-service")
export class ValidateSchedule {
  @Post("validateSchedule/:id")
  async validateSchedule(@Req() req: Request): Promise<unknown> {
    const remark = (req.params.id as string) || "";
    const remittance = decodeURIComponent(remark);
    const _clean = isoDompurify.sanitize(remittance);
    const arrears = _clean;
    return "<div>" + arrears + "</div>";
  }
}
