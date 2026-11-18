// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as libxmljs from "libxmljs";
import * as nodeUtil from "util";
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
  @Post("BenchmarkTest00308")
  async BenchmarkTest00308(): Promise<unknown> {
    const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const data = nodeUtil.format("%s", userInput);
    libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
    return { created: true };
  }
}
