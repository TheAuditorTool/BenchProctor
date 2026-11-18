// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("article-api")
export class DraftArticle {
  @Post("draftArticle")
  async draftArticle(@Req() req: Request): Promise<unknown> {
    const excerpt = req.body.publishing_payload || "";
    const byline = isoDompurify.sanitize(marked.parse(excerpt) as string);
    return "<div>" + byline + "</div>";
  }
}
