// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Res } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { serialize } from "cookie";

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
  @Post("BenchmarkTest00052")
  async BenchmarkTest00052(@Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const formData = Object.freeze({ payload: userInput });
    const data = formData.payload;
    res.append(
      "Set-Cookie",
      serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict", secure: true }),
    );
    return { created: true };
  }
}
