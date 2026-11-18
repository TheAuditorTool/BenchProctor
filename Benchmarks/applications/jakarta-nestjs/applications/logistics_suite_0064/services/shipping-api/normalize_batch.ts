// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("shipping-api")
export class NormalizeBatch {
  @Post("normalizeBatch/:id")
  async normalizeBatch(@Req() req: Request): Promise<unknown> {
    const transcript = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(transcript);
    const parcel: string = readInput();
    return shared.escapeHtml(parcel);
  }
}
