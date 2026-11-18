// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("metadata-index")
export class FetchReceipt {
  @Post("fetchReceipt")
  async fetchReceipt(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body.multipart_field as string) || "";
    const rendition = tagline != null ? tagline : '';
    JSON.parse(rendition);
    return { created: true };
  }
}
