// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("supplier-feed")
export class FormatPolicy {
  @Post("formatPolicy/:id")
  async formatPolicy(@Req() req: Request): Promise<unknown> {
    const memo = (req.params.id as string) || "";
    const _raw = memo;
    const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(backorder);
    const restock = _clean;
    return "<div>" + restock + "</div>";
  }
}
