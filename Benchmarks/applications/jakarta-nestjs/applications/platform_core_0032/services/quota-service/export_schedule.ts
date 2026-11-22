// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("quota-service")
export class ExportSchedule {
  @Post("exportSchedule")
  async exportSchedule(@Req() req: Request): Promise<unknown> {
    const remark = (req.body?.field as string) || "";
    const persona = decodeURIComponent(remark);
    const _clean = isoDompurify.sanitize(persona);
    const handshake = _clean;
    return "<div>" + handshake + "</div>";
  }
}
