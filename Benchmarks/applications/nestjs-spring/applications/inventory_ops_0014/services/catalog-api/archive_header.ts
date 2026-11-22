// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("catalog-api")
export class ArchiveHeader {
  @Post("archiveHeader/:id")
  async archiveHeader(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.params.id as string) || "";
    let restock: string = '';
    const onInput = (v: string): void => { restock = v; };
    onInput(excerpt);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: restock });
    return page;
  }
}
