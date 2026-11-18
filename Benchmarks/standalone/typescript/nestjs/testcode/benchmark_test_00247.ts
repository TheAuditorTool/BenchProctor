// SPDX-License-Identifier: Apache-2.0
import { Controller, Header, Post } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
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
  @Post("BenchmarkTest00247")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00247(): Promise<unknown> {
    const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    return "<div>" + data + "</div>";
  }
}
