// SPDX-License-Identifier: Apache-2.0
import { Controller, Header, Post } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as nodeUtil from "util";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00606")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00606(): Promise<unknown> {
    const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const data = nodeUtil.format("%s", userInput);
    const processed = isoDompurify.sanitize(marked.parse(data) as string);
    return "<div>" + processed + "</div>";
  }
}
